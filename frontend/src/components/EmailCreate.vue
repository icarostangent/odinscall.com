<template>
    <div id="createEmailForm">
        <form class="mb-3">
            <div class="form-control">
                <input class="form-control" type="text" v-model="email" name="email" placeholder="Email" />
                <button @click.prevent="onClickCreate" type="button" class="btn btn-primary btn-sm">Save</button>
            </div>
        </form>
    </div>
</template>

<script>
export default {
    name: 'EmailCreate',
    data() {
        return {
            email: '',
        }
    },
    methods: {
        onClickCreate() {
            const emailPattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

            if (!emailPattern.test(this.email)) {
                this.$store.commit("SET_MESSAGE", { title: "Error", text: "Invalid email", display: true, style: "bg-warning" })
                return
            }
            this.$store.dispatch('createEmail', { 'email': this.email })
                .then(() => {
                    this.$store.state.emails.totalItems += 1
                    this.email = ''
                    this.$store.commit("SET_MESSAGE", { title: "Success", text: "Email created successfully", display: true, style: "bg-success" })
                })
                .catch((e) => {
                    this.$store.commit("SET_MESSAGE", { title: "Error", text: e.response.data.detail, display: true, style: "bg-warning" })
                })

        }
    },
}
</script>
